package Exceptions;

@SuppressWarnings("serial")


public class CatalogoExceptions extends Exception {
	
	private int cantidad;
	private String objeto;

    public void NegativoException( int cantidad, String objeto)
    {
        this.cantidad = cantidad;
        this.objeto = objeto;
    }

    @Override
    public String getMessage( )
    {
        return "No puede haber " + cantidad + " " + objeto;
    }

}
