package GestionEmpleados;

import java.util.HashMap;

public class Cliente extends Usuario {
	
	public static HashMap<String, String> usuariosClientes = new HashMap<>();
	protected static HashMap<String, String> contrasenasClientes = new HashMap<>();
	protected static HashMap<String, Cliente> clientesInfoCompletitud = new HashMap<>();
	
	

	public Cliente(String nombre, String password, String login) {
		super(nombre, password, login);
		if (usuariosClientes.containsKey(login)) {
			throw new IllegalArgumentException("Error: el login '" + login + "' ya está en uso por otro cliente.");
		}
		usuariosClientes.put(login, nombre); 
		contrasenasClientes.put(login, password); 
	}
	
	public void anadirClienteInfo() {
		clientesInfoCompletitud.put(login, this);
	}
	

	
	//Ver turnos
	//Ver sitrio de trabajo

}
