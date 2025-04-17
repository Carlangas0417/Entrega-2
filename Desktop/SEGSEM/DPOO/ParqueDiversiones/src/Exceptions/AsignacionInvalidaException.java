package Exceptions;


public class AsignacionInvalidaException extends Exception {
	private static final long serialVersionUID = 1L;
    public AsignacionInvalidaException(String mensaje) {
        super(mensaje);
    }
}
