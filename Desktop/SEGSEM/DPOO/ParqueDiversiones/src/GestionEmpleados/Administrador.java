package GestionEmpleados;

import java.util.List;

public class Administrador extends Empleado {

	public Administrador(String nombre, String id, String password, String login, List<Turno> turnosAsignados) {
		super(nombre, id, password, login, turnosAsignados);
	}
	
	
	public void asignarLugarServicio(ACajero empleado, LugarServicio sitio) throws Exception{
	}
	
	public void asignarOperador() {
			
		}
	
	//asignar empleado a atracción
	//asignar empleado a cafeteria
	// tienda, taquilla
	
	

}
