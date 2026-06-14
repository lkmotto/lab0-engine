def init_circuit(spec):
    from PySpice.Spice.Netlist import Circuit
    
    r_val = spec.get('r_val', '1k')
    c_val = spec.get('c_val', '1uF')
    
    circuit = Circuit(spec.get('name', 'RC Filter'))
    circuit.V('input', 'Vin', circuit.gnd, 'DC 0 AC 1')
    circuit.R('1', 'Vin', 'Vout', r_val)
    circuit.C('1', 'Vout', circuit.gnd, c_val)
    
    return circuit

