package GestionEmpleados;

import java.util.List;

public class Cafeteria extends LugarServicio{
	
	public final static String CAFETERIA = "CAFETERIA";
	public String tipo;
	public List<Cocinero> cocineros;

	public Cafeteria(ACajero cajeroAsignado, String ubicacion, List<Cocinero> cocineros) {
		super(cajeroAsignado, ubicacion, CAFETERIA);
		this.cocineros = cocineros;
	}
	
	public void añadirCocinero(Cocinero cocinero) {
	    if (cocinero != null) {
	        cocineros.add(cocinero);
	        System.out.println("Cocinero añadido correctamente: " + cocinero.getNombre());
	    } else {
	        System.out.println("No se puede añadir un cocinero nulo.");
	    }
	}


}
