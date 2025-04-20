package VentaTiquetes;

import java.io.Serializable;

import CatalogoAtracciones.Atraccion;
import Util.Fecha;

public class Individual implements TipoTiquete, Serializable {

    private static final long serialVersionUID = 1L;

    private Atraccion atraccionParticular;

    public Individual(Atraccion atraccionParticular) {
        this.atraccionParticular = atraccionParticular;
    }

    public Atraccion getAtraccionParticular() {
        return atraccionParticular;
    }

    public void setAtraccionParticular(Atraccion atraccion) {
        this.atraccionParticular = atraccion;
    }


    @Override
    public boolean esValidoParaFecha(Fecha fecha) {
        return true;
    }

    @Override
    public boolean permiteAcceso(Atraccion atraccion) {
        return atraccion.equals(this.atraccionParticular);
    }

    @Override
    public String tipo() {
        return "Individual";
    }
}