import os
import requests
import json
from lab0.trust import Check, uncalibrated


def order_part(stl_path, spec, quantity=1, shipping_info=None):
    """
    Dispatch verified mechanical designs to Slant 3D API for on-demand fabrication.
    Assumes SLANT3D_API_KEY is available in the environment (e.g. injected by Doppler).
    """
    api_key = os.environ.get("SLANT3D_API_KEY")
    if not api_key:
        return uncalibrated(
            "slant3d_api",
            {
                "dispatch_checks": {
                    "api_auth": Check(
                        passed=False,
                        detail="SLANT3D_API_KEY environment variable not set.",
                    )
                }
            },
        )

    api_url = os.environ.get(
        "SLANT3D_API_URL", "https://api.slant3dapi.com/api/v1/orders"
    )

    metadata = {
        "material": spec.get("material", "PLA"),
        "color": spec.get("color", "Black"),
        "quantity": quantity,
        "shipping_info": shipping_info or {},
    }

    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        with open(stl_path, "rb") as f:
            files = {
                "file": (os.path.basename(stl_path), f, "application/vnd.ms-pki.stl")
            }
            data = {"metadata": json.dumps(metadata)}

            response = requests.post(api_url, headers=headers, files=files, data=data)

        if response.status_code in (200, 201, 202):
            order_data = response.json()
            checks = {
                "order_placed": Check(
                    passed=True,
                    detail=f"Order successfully placed with Slant 3D. Order ID: {order_data.get('order_id', 'unknown')}",
                )
            }
            return uncalibrated("slant3d_api", {"dispatch_checks": checks})
        else:
            return uncalibrated(
                "slant3d_api",
                {
                    "dispatch_checks": {
                        "api_error": Check(
                            passed=False,
                            detail=f"API returned {response.status_code}: {response.text}",
                        )
                    }
                },
            )

    except requests.exceptions.RequestException as e:
        return uncalibrated(
            "slant3d_api",
            {
                "dispatch_checks": {
                    "network_error": Check(
                        passed=False, detail=f"Connection error: {str(e)}"
                    )
                }
            },
        )
    except Exception as e:
        return uncalibrated(
            "slant3d_api",
            {"dispatch_checks": {"system_error": Check(passed=False, detail=str(e))}},
        )
