package VentaTiquetes;

import java.io.Serializable;

import CatalogoAtracciones.Atraccion;
import Util.Fecha;
import Util.RangoFechas;

public class Temporada implements TipoTiquete, Serializable {

    private static final long serialVersionUID = 1L;

    private RangoFechas rangoFechas;
    private int descuentoAplicado;

    public Temporada(RangoFechas rangoFechas, int descuentoAplicado) {
        this.rangoFechas = rangoFechas;
        this.descuentoAplicado = descuentoAplicado;
    }

    public RangoFechas getRangoFechas() {
        return rangoFechas;
    }

    public int getDescuentoAplicado() {
        return descuentoAplicado;
    }

    public void setRangoFechas(RangoFechas rangoFechas) {
        this.rangoFechas = rangoFechas;
    }

    public void setDescuentoAplicado(int descuentoAplicado) {
        this.descuentoAplicado = descuentoAplicado;
    }

    @Override
    public boolean esValidoParaFecha(Fecha fecha) {
        return rangoFechas.incluye(fecha);
    }

    @Override
    public boolean permiteAcceso(Atraccion atraccion) {
        return true;
    }

    @Override
    public String tipo() {
        return "Temporada";
    }
}
