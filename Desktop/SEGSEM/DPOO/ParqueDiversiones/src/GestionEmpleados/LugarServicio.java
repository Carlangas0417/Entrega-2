package GestionEmpleados;

public class LugarServicio {
	private ACajero cajeroAsignado;
	private String ubicacion; 

	public LugarServicio(ACajero cajeroAsignado, String ubicacion) {
		super();
		this.cajeroAsignado = cajeroAsignado;
		this.ubicacion = ubicacion;
	}

	public ACajero getCajeroAsignado() {
		return cajeroAsignado;
	}
	
	public String getUbicacion() {
		return ubicacion;
	}

	public void setCajeroAsignado(ACajero cajeroAsignado) {
		this.cajeroAsignado = cajeroAsignado;
	} 
	
	
	
}
