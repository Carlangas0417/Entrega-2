package CatalogoAtracciones;

import java.util.List;

import GestionEmpleados.Empleado;
import GestionEmpleados.Operador;

public class Mecanica extends Atraccion{
	

	public double alturaMinima;
	public double alturaMaxima;
	public double pesoMinimo;
	public double pesoMaximo;
	public List<String> contraindicaciones;
	public String nivelRiesgo;
	
	public Mecanica(String nombre, String ubicacion, int cupoMax, int empleadosMin, String nivelExclusividad,
			List<String> disponibleClima, double alturaMaxima, double alturaMinima, double pesoMaximo, double pesoMinimo,
			List<String> contraindicaciones, String nivelRiesgo, List<Empleado> empleados) {
		super(nombre, ubicacion, cupoMax, empleadosMin, nivelExclusividad, disponibleClima, empleados);
		this.alturaMaxima = alturaMaxima; 
		this.alturaMinima = alturaMinima;
		this.pesoMaximo = pesoMaximo;
		this.pesoMinimo = pesoMinimo;
		this.contraindicaciones = contraindicaciones;
		this.nivelRiesgo = nivelRiesgo;
	}

	public double getAlturaMinima() {
		return alturaMinima;
	}

	public double getAlturaMaxima() {
		return alturaMaxima;
	}

	public double getPesoMinimo() {
		return pesoMinimo;
	}

	public double getPesoMaximo() {
		return pesoMaximo;
	}

	public List<String> getContraindicaciones() {
		return contraindicaciones;
	}

	public String getNivelRiesgo() {
		return nivelRiesgo;
	}
	
	@Override
	public void asignarEmpleado(Empleado empleado) {
	    if (empleado instanceof Operador) {
	        System.out.println("El empleado es un Operador.");
	        Operador operador = (Operador) empleado;
	        
	        if (this.nivelRiesgo.equals("ALTO")) {
	        	if (operador.getAtraccionesEntrenado().contains(this.id)) {
	        		
	        	}
	        } 
	        
	        else {
	        	System.out.println("El empleado seleccionado no está capacitado para la atracción.");
	        }

	    }
	    else {
	        System.out.println("El empleado NO es un Operador.\n");
	        System.out.println("No se puede asignar el empleado deseado a la atracción.\n");
        }
	}
	
	
	
	
	public void mostrarMecanica() {
	    System.out.println("Detalles de la atracción Mecánica:");
	    System.out.println("Nombre: " + getNombre());
	    System.out.println("Ubicación: " + getUbicacion());
	    System.out.println("Cupo Máximo: " + getCupoMax());
	    System.out.println("Empleados Mínimos: " + getEmpleadosMin());
	    System.out.println("Nivel de Exclusividad: " + getNivelExclusividad());
	    System.out.println("Clima Disponible: " + getDisponibleClima());
	    System.out.println("Altura Mínima: " + getAlturaMinima() + " metros");
	    System.out.println("Altura Máxima: " + getAlturaMaxima() + " metros");
	    System.out.println("Peso Mínimo: " + getPesoMinimo() + " kg");
	    System.out.println("Peso Máximo: " + getPesoMaximo() + " kg");
	    
	    if (getContraindicaciones() != null && !getContraindicaciones().isEmpty()) {
	        System.out.println("Contraindicaciones: ");
	        for (String contraindicacion : getContraindicaciones()) {
	            System.out.println("- " + contraindicacion);
	        }
	    } else {
	        System.out.println("No hay contraindicaciones.");
	    }
	    
	    System.out.println("Nivel de Riesgo: " + getNivelRiesgo());
	}

	
	
	
	
	

}
