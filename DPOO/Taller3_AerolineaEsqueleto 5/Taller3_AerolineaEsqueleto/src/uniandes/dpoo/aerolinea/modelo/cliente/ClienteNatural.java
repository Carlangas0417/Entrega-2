package uniandes.dpoo.aerolinea.modelo.cliente;

public class ClienteNatural extends Cliente{
	public static final String NATURAL = "Natural";
	private String nombre;
	private String Cedula; //Implementado para identificador
	
	public ClienteNatural(String nombre) {
		this.nombre = nombre;
	}

	public String getNombre() {
		return nombre;
	}

	public String getIdentificador() {
		return Cedula;
	}

	public String getTipoCliente() {
		return NATURAL;
	}
	
	
	
	

}
