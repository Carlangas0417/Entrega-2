package GestionEmpleados;

import java.util.List;

public class Empleado extends Usuario{
	
	protected List<Turno> turnosAsignados;

	public Empleado(String nombre, String id, String password, String login, List<Turno> turnosAsignados) {
		super(nombre, id, password, login);
		this.turnosAsignados = turnosAsignados;
	}
	
	//Ver turnos
	//Ver sitrio de trabajo
	
	
	
	
	
	
}
