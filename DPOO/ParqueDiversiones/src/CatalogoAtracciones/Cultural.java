package CatalogoAtracciones;

import java.util.List;

public class Cultural extends Atraccion{
	public Cultural(String nombre, String ubicacion, int cupoMax, int empleadosMin, NivelesValidos nivelExclusividad,
			List<String> disponibleClima) {
		super(nombre, ubicacion, cupoMax, empleadosMin, nivelExclusividad, disponibleClima);
		// TODO Auto-generated constructor stub
	}

	public int edadMinima;

}
