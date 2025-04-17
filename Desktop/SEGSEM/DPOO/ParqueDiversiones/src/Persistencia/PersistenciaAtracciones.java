package Persistencia;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;

import org.json.JSONArray;
import org.json.JSONObject;

import CatalogoAtracciones.Atraccion;



public class PersistenciaAtracciones {
	private static final String ID = "id";
    private static final String NOMBRE = "nombreAtraccion";
    private static final String UBICACION = "ubicacion";
    private static final String CUPO_MAX = "cupoMax";
    private static final String EMPLEADOS_MIN = "empleadosMin";
    private static final String NIVEL_EXCLUSIVIDAD = "nivelExclusividad";
    private static final String DISPO_CLIMA = "disponibleClima";
    private static final String PRESTA_SERVICIO = "prestaServicio";
    private static final String EMPLEADOS = "empleados";
    
    public void cargarAtraccion(String archivo, Atraccion atraccion) throws IOException
    {
        String jsonCompleto = new String( Files.readAllBytes( new File( archivo ).toPath( ) ) );
        JSONObject raiz = new JSONObject( jsonCompleto );

        cargarAtraccionesCreadas(atraccion, raiz.getJSONArray("atracciones") );
        cargarRelacionesCreadas(atraccion, raiz.getJSONArray("relaciones") );
    }
    
    public void salvarTiquetes( String archivo, Atraccion atraccion) throws IOException
    {
        JSONObject jobject = new JSONObject( );

        salvarAtracciones( atraccion, jobject );

        // Salvar tiquetes
        salvarRelaciones( atraccion, jobject );

        // Escribir la estructura JSON en un archivo
        PrintWriter pw = new PrintWriter( archivo );
        jobject.write( pw, 2, 0 );
        pw.close( );
    }
    
    private void cargarClientes( Atraccion atraccion, JSONArray jClientes )
    {
        int numClientes = jClientes.length( );
        for( int i = 0; i < numClientes; i++ )
        {
            JSONObject cliente = jClientes.getJSONObject( i );
            String tipoCliente = cliente.getString( TIPO_CLIENTE );
            Cliente nuevoCliente = null;
            
            if( ClienteNatural.NATURAL.equals( tipoCliente ) )
            {
              
                String nombre = cliente.getString( NOMBRE_CLIENTE );
                nuevoCliente = new ClienteNatural( nombre );
            }
            else
            {
                // 2. En esta estrategia, en la clase ClienteCorporativo se realiza una parte de lo que tiene que ver con cargar objetos de la clase ClienteCorporativo.
                // La clase ClienteCorporativo tiene un método para cargar y otro para salvar.
                // En este caso, la persistencia es una preocupación de la cual se ocupa la clase ClienteCorporativo
                nuevoCliente = ClienteCorporativo.cargarDesdeJSON( cliente );
            }
            if( !aerolinea.existeCliente( nuevoCliente.getIdentificador( ) ) )
                aerolinea.agregarCliente( nuevoCliente );
            else
                throw new ClienteRepetidoException( nuevoCliente.getTipoCliente( ), nuevoCliente.getIdentificador( ) );
        }
    }

}
