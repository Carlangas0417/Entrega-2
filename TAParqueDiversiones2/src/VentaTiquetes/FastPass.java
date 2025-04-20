package VentaTiquetes;

import java.io.Serializable;

import CatalogoAtracciones.Atraccion;
import Util.Fecha;

public class FastPass implements TipoTiquete, Serializable {

    private static final long serialVersionUID = 1L;

    private Fecha fecha;

    public FastPass(Fecha fecha) {
        this.fecha = fecha;
    }

    public Fecha getFecha() {
        return fecha;
    }

    public void setFecha(Fecha fecha) {
        this.fecha = fecha;
    }


    @Override
    public boolean esValidoParaFecha(Fecha f) {
        return this.fecha.esIgualA(f);
    }

    @Override
    public boolean permiteAcceso(Atraccion atraccion) {
        return true;
    }

    @Override
    public String tipo() {
        return "FastPass";
    }
}
