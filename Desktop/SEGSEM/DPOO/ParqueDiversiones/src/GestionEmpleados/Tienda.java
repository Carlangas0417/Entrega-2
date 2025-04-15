package GestionEmpleados;

public class Tienda extends LugarServicio{
	
	public final static String TIENDA = "TIENDA";
	public String tipo;
	
	public Tienda(ACajero cajeroAsignado, String ubicacion) {
		super(cajeroAsignado, ubicacion, TIENDA);
	}

	
	
}
