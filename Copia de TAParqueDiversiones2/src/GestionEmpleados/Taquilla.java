package GestionEmpleados;

public class Taquilla extends LugarServicio{
	
	public static final String TAQUILLA = "TAQUILLA";
	public String tipo; 
	
	public Taquilla(ACajero cajeroAsignado, String ubicacion) {
		super(cajeroAsignado, ubicacion, TAQUILLA);
	}
	
	
}
