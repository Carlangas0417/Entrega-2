package GestionEmpleados;

import java.util.List;

public class Cocinero extends ACajero{

	public Cocinero(String nombre, String password, String login, List<Turno> turnosAsignados,
			LugarServicio lugarServicio) {
		super(nombre, password, login, turnosAsignados, lugarServicio);
	}
	
}
