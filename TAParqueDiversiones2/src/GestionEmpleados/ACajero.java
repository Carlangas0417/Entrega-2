package GestionEmpleados;

import java.util.List;

public class ACajero extends Empleado {
	
	private LugarServicio lugarServicio;

	public ACajero(String nombre, String id, String password, String login, List<Turno> turnosAsignados, LugarServicio lugarServicio) {
		super(nombre, id, password, login, turnosAsignados);
		this.lugarServicio = lugarServicio;
	}

	public LugarServicio getLugarServicio() {
		return lugarServicio;
	}

	public void setLugarServicio(LugarServicio lugarServicio) {
		this.lugarServicio = lugarServicio;
	}
	
	
	
	

}
