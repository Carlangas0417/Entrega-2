package GestionEmpleados;

import java.util.List;

public class Cocinero extends ACajero{

	public Cocinero(String nombre, String id, String password, String login, List<Turno> turnosAsignados,
			LugarServicio lugarServicio) {
		super(nombre, id, password, login, turnosAsignados, lugarServicio);
	}
	
}
