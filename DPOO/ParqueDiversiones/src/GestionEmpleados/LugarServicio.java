package GestionEmpleados;

public class LugarServicio {
	private ACajero cajeroAsignado;
	private String ubicacion; 
	private String tipo; 

	public LugarServicio(ACajero cajeroAsignado, String ubicacion, String tipo) {
		super();
		this.cajeroAsignado = cajeroAsignado;
		cajeroAsignado.setLugarServicio(this);
		this.ubicacion = ubicacion;
		this.tipo = tipo;
	}

	public ACajero getCajeroAsignado() {
		return cajeroAsignado;
	}
	
	public String getUbicacion() {
		return ubicacion;
	}

	public void asignarCajero(ACajero nuevoCajero) {
	    if (nuevoCajero != null) {
	        this.cajeroAsignado = nuevoCajero;
	        nuevoCajero.setLugarServicio(this);
	        System.out.println("Cajero asignado correctamente: " + nuevoCajero.getNombre());
	    } else {
	        System.out.println("No se puede asignar un cajero nulo.");
	    }
	}

	
	public String getTipo() {
		return this.tipo; 
	}
	
	
	
}
