package GestionEmpleados;

import java.util.HashMap;
import java.util.List;

public class Empleado extends Usuario {
	
	public static HashMap<String, String> usuariosEmpleados = new HashMap<>();
	protected static HashMap<String, String> contrasenasEmpleados = new HashMap<>();
	protected List<Turno> turnosAsignados;
	protected static HashMap<String, Cliente> cempleadosInfoCompletitud = new HashMap<>();

	public Empleado(String nombre, String password, String login, List<Turno> turnosAsignados) {
		super(nombre, password, login);
		
		if (usuariosEmpleados.containsKey(login)) {
			throw new IllegalArgumentException("Error: el login '" + login + "' ya está en uso por otro empleado.");
		}
		
		this.turnosAsignados = turnosAsignados;
		usuariosEmpleados.put(login, nombre); 
		contrasenasEmpleados.put(login, password); 
	}

	
	//Ver turnos
	//Ver sitrio de trabajo

}
