package VentaTiquetes;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import CatalogoAtracciones.Atraccion;
import Util.Fecha; 

public abstract class Tiquete implements Serializable {

    private static final long serialVersionUID = 1L;

    private static int contadorId = 1;

    private final int id;
    private Fecha fechaVenta;
    private String exclusividad;
    private boolean usado;
    private List<TipoTiquete> modalidades;

    public Tiquete(Fecha fechaVenta, String exclusividad) {
        this.id = contadorId++;
        this.fechaVenta = fechaVenta;
        this.exclusividad = exclusividad;
        this.usado = false;
        this.modalidades = new ArrayList<>();
    }

    public int getId() {
        return id;
    }

    public Fecha getFechaVenta() {
        return fechaVenta;
    }

    public String getExclusividad() {
        return exclusividad;
    }

    public boolean isUsado() {
        return usado;
    }

    public List<TipoTiquete> getModalidades() {
        return modalidades;
    }

    public void setFechaVenta(Fecha fechaVenta) {
        this.fechaVenta = fechaVenta;
    }

    public void setExclusividad(String exclusividad) {
        this.exclusividad = exclusividad;
    }

    public void setUsado(boolean usado) {
        this.usado = usado;
    }

    public void setModalidades(List<TipoTiquete> modalidades) {
        this.modalidades = modalidades;
    }

    public void agregarModalidad(TipoTiquete modalidad) {
        this.modalidades.add(modalidad);
    }

    public boolean esValidoParaFecha(Fecha fecha) {
        for (TipoTiquete tipo : modalidades) {
            if (!tipo.esValidoParaFecha(fecha)) {
                return false;
            }
        }
        return true;
    }

    // Validación: ¿permite acceder a una atracción?
    public boolean permiteAcceso(Atraccion atraccion) {
        String atraccionExclusividad = atraccion.getNivelExclusividad(); 
        if (!puedeAccederPorExclusividad(atraccionExclusividad)) {
            return false;
        }

        for (TipoTiquete tipo : modalidades) {
            if (!tipo.permiteAcceso(atraccion)) {
                return false;
            }
        }

        return true;
    }

    // Lógica de acceso por exclusividad
    private boolean puedeAccederPorExclusividad(String atraccionExclusividad) {
        if (this.exclusividad == "DIAMANTE") return true;
        if (this.exclusividad == "ORO" && atraccionExclusividad != "DIAMANTE") return true;
        if (this.exclusividad == "FAMILIAR" && atraccionExclusividad == "FAMILIAR") return true;
        return false;
    }
}