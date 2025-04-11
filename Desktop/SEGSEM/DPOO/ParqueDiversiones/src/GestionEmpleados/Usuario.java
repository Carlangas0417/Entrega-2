package GestionEmpleados;

import java.util.HashMap;

public abstract class Usuario {
	
	public String nombre;
	public String id;
	protected String password;
	protected String login;
	protected static HashMap<String, String> contrasenas;
	protected static HashMap<String, String> usuarios;
	
	//protected List <Tiquetes> tiquetesDisponibles;
	
	public Usuario(String nombre, String id, String password, String login) {
		if (usuarios.containsKey(login)) {
			throw new IllegalArgumentException("Error: el login '" + login + "' ya está en uso.");
		}
		this.nombre = nombre;
		this.id = id;
		this.password = password;
		this.login = login;
		
		usuarios.put(nombre, login);
		contrasenas.put(login, password); 
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getLogin() {
		return login;
	}

	public void setLogin(String login) {
		this.login = login;
	}
	
	
	
	
	
}


