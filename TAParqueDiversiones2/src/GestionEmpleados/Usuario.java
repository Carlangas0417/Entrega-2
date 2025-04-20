package GestionEmpleados;

import java.util.ArrayList;
import java.util.List;

import Tiquetes.Tiquete;

public abstract class Usuario {
	
	private static int contadorIds = 0;
	public String nombre;
	public String id;
	protected String password;
	protected String login;
	protected List <Tiquete> tiquetesDisponibles;
	
	public Usuario(String nombre, String password, String login) {
		this.nombre = nombre;
		this.id = String.valueOf(contadorIds); 
        contadorIds++; 
		this.password = password;
		this.login = login;
		this.tiquetesDisponibles = new ArrayList<>();

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
	
	public List<Tiquete> getTiquetesDisponibles(){
		return tiquetesDisponibles;
	}
	
	
	
	
	
}


