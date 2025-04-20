package VentaTiquetes;

import java.io.Serializable;

import CatalogoAtracciones.Atraccion;
import Util.Fecha;

public interface TipoTiquete extends Serializable {

	boolean esValidoParaFecha(Fecha fecha);

    boolean permiteAcceso(Atraccion atraccion);

    String tipo();  
}
