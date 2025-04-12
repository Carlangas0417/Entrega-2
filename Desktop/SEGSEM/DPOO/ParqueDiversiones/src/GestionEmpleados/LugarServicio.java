package GestionEmpleados;

public class LugarServicio {
	private ACajero cajeroAsignado;

	public LugarServicio(ACajero cajeroAsignado) {
		super();
		this.cajeroAsignado = cajeroAsignado;
	}

	public ACajero getCajeroAsignado() {
		return cajeroAsignado;
	}

	public void setCajeroAsignado(ACajero cajeroAsignado) {
		this.cajeroAsignado = cajeroAsignado;
	} 
	
	
	
}
