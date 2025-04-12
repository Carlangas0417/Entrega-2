package uniandes.dpoo.aerolinea.modelo;

/**
 * Esta clase tiene la información de una ruta entre dos aeropuertos que cubre una aerolínea.
 */
public class Ruta
{
    // TODO completar
	private Aeropuerto destino;
	private Aeropuerto origen;
	private String horaSalida;
	private String horaLlegada;
	private String codigoRuta;
	

    public Ruta(Aeropuerto destino, Aeropuerto origen, String horaSalida, String horaLlegada, String codigoRuta) {
		this.destino = destino;
		this.origen = origen;
		this.horaSalida = horaSalida;
		this.horaLlegada = horaLlegada;
		this.codigoRuta = codigoRuta;
	}
    

    public Aeropuerto getDestino() {
		return destino;
	}


	public Aeropuerto getOrigen() {
		return origen;
	}


	public String getHoraSalida() {
		return horaSalida;
	}


	public String getHoraLlegada() {
		return horaLlegada;
	}


	public String getCodigoRuta() {
		return codigoRuta;
	}


	public int getDuracion() {
    	int minutosOrigen= getMinutos(horaSalida)+getHoras(horaSalida)*60;
    	int minutosDestino= getMinutos(horaLlegada)+getHoras(horaLlegada)*60;
    	return minutosDestino-minutosOrigen;
    }
	/**
     * Dada una cadena con una hora y minutos, retorna los minutos.
     * 
     * Por ejemplo, para la cadena '715' retorna 15.
     * @param horaCompleta Una cadena con una hora, donde los minutos siempre ocupan los dos últimos caracteres
     * @return Una cantidad de minutos entre 0 y 59
     */
   
    public static int getMinutos( String horaCompleta )
    {
        int minutos = Integer.parseInt( horaCompleta ) % 100;
        return minutos;
    }

    /**
     * Dada una cadena con una hora y minutos, retorna las horas.
     * 
     * Por ejemplo, para la cadena '715' retorna 7.
     * @param horaCompleta Una cadena con una hora, donde los minutos siempre ocupan los dos últimos caracteres
     * @return Una cantidad de horas entre 0 y 23
     */
    public static int getHoras( String horaCompleta )
    {
        int horas = Integer.parseInt( horaCompleta ) / 100;
        return horas;
    }

    
}
