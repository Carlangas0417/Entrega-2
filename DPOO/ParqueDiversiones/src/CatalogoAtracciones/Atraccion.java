package CatalogoAtracciones;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import GestionEmpleados.Empleado;

public abstract class Atraccion implements Serializable{
	
	private static int contadorId = 1; 
    public final int id; 
	public String nombre;
	public String ubicacion;
	public int cupoMax;
	public int empleadosMin;
	public String nivelExclusividad;
	public List<String> disponibleClima;
	public boolean prestaServicio;
	public List<Empleado> empleados;
	

	public Atraccion(String nombre, String ubicacion, int cupoMax, int empleadosMin,
			String nivelExclusividad, List<String> disponibleClima, List<Empleado> empleados) {
		this.id = contadorId++;
		this.nombre = nombre;
		this.ubicacion = ubicacion;
		this.cupoMax = cupoMax;
		this.empleadosMin = empleadosMin;
		this.nivelExclusividad = nivelExclusividad;
		this.disponibleClima = new ArrayList<>();
		this.empleados = empleados;
		
		if (this.empleados != null) {
		
			if (this.empleados.size() >= empleadosMin) {
				this.prestaServicio = true;
			}
			else {
				this.prestaServicio = false;
			}
		}
		else {
			this.prestaServicio = false;
		}
		this.empleados = new ArrayList<>();
		
	}
	
	public int getID() {
		return this.id;
	}
	
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
	
	public String getNivelExclusividad() {
		return nivelExclusividad;
	}
	
	public void setNivelExclusividad(String nivelExclusividad) {
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
	
	public List<Empleado> getEmpleados(){
		return this.empleados;
	}
	
	public void anadirClima(String clima) {
		this.disponibleClima.add(clima);
	}
	
	public void agregarEmpleado(Empleado empleado) {
		this.empleados.add(empleado);
		System.out.print("Se ha agregado un nuevo empleado a la lista.\n");
		if (!prestaServicio && this.empleados.size() >= empleadosMin) {
				this.prestaServicio = true;
				System.out.print("Como ahora hay " + this.empleados.size() + " empleado(s) y el mínimo de empleados es " + getEmpleadosMin() + " la atracción presta servicio.\n");
		}
	}
	
	public void mostrarAtraccion() {
		
	}

     
}