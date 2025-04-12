package CatalogoAtracciones;

import java.util.List;

public class Mecanica extends Atraccion{
	

	public double alturaMinima;
	public double alturaMaxima;
	public double pesoMinimo;
	public double pesoMaximo;
	public List<String> contraindicaciones;
	public String nivelRiesgo;
	
	public Mecanica(String nombre, String ubicacion, int cupoMax, int empleadosMin, NivelesValidos nivelExclusividad,
			List<String> disponibleClima, double alturaMaxima, double alturaMinima, double pesoMaximo, double pesoMinimo,
			List<String> contraindicaciones, String nivelRiesgo) {
		super(nombre, ubicacion, cupoMax, empleadosMin, nivelExclusividad, disponibleClima);
		this.alturaMaxima = alturaMaxima; 
		this.alturaMinima = alturaMinima;
		this.pesoMaximo = pesoMaximo;
		this.pesoMinimo = pesoMinimo;
		this.contraindicaciones = contraindicaciones;
		this.nivelRiesgo = nivelRiesgo;
		// TODO Auto-generated constructor stub
	}
	
	
	
	

}
