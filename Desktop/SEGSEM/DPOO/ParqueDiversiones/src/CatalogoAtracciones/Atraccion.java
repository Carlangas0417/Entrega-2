package CatalogoAtracciones;

import java.util.List;
import java.util.Scanner;

import GestionEmpleados.Empleado;

public abstract class Atraccion {
	
	public String nombre;
	public String ubicacion;
	public int cupoMax;
	public int empleadosMin;
	public NivelesValidos nivelExclusividad;
	public List<String> disponibleClima;
	public boolean prestaServicio;
	public List<Empleado> empleados;
	

	public Atraccion(String nombre, String ubicacion, int cupoMax, int empleadosMin,
			NivelesValidos nivelExclusividad, List<String> disponibleClima) {
		this.nombre = nombre;
		this.ubicacion = ubicacion;
		this.cupoMax = cupoMax;
		this.empleadosMin = empleadosMin;
		this.nivelExclusividad = nivelExclusividad;
		this.disponibleClima = disponibleClima; //revisar eso mejor
		if (this.empleados.size() >= empleadosMin) {
			this.prestaServicio = true;
		}
		else {
			this.prestaServicio = false;
		}
		
	}
	
	public enum NivelesValidos {
		BASICO, DIAMANTE, ORO, FAMILIAR;
	}
	//public void asignarEmpleado();
	
	public String getNombre() {
		return nombre;
	}
	
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	public String getUbicacion() {
		return ubicacion;
	}
	
	public void setUbicacion(String ubicacion) {
		this.ubicacion = ubicacion;
	}
	
	public int getCupoMax() {
		return cupoMax;
	}
	
	public void setCupoMax(int cupoMax) {
		this.cupoMax = cupoMax;
	}
	
	public int getEmpleadosMin() {
		return empleadosMin;
	}
	
	public void setEmpleadosMin(int empleadosMin) {
		this.empleadosMin = empleadosMin;
	}
	
	public NivelesValidos getNivelExclusividad() {
		return nivelExclusividad;
	}
	
	public void setNivelExclusividad(NivelesValidos nivelExclusividad) {
		this.nivelExclusividad = nivelExclusividad;
	}
	
	public List<String> getDisponibleClima() {
		return disponibleClima;
	}
	
	public void setDisponibleClima(List<String> disponibleClima) {
		this.disponibleClima = disponibleClima;
	}
	
	public boolean isPrestaServicio() {
		return prestaServicio;
	}
	
	public void setPrestaServicio(boolean prestaServicio) {
		this.prestaServicio = prestaServicio;
	}
	
	public void agregarEmpleado(Empleado empleado) {
		this.empleados.add(empleado);
		System.out.print("Se ha agregado un nuevo empleado a la lista.");
		if (!prestaServicio && this.empleados.size() >= empleadosMin) {
				this.prestaServicio = true;
				System.out.print("Como ahora hay " + this.empleados.size() + "la atracción presta servicio.");
		}
	}
	
	public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Consola para crear una nueva atracción");
        System.out.print("¿Que tipo de atracción desea?");
        System.out.print("1. Mecánica");
        System.out.print("2. Cultural");
        System.out.print("3. Espectáculo");
	}
        

     
	
}