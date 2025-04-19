package ConsolaGeneral;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;

public class CGeneral {
	
	
	

    protected String cadena(String mensaje)
    {
        try
        {
            System.out.print(mensaje + ": ");
            System.out.flush(); 
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            String input = reader.readLine();
            return input;
        }
        catch(IOException e)
        {
            System.out.println("Hubo un error al leer la consola.");
        }
        return "error";
    }

    protected boolean pedirConfirmacionAlUsuario( String mensaje )
    {
        try
        {
            System.out.print( mensaje + " (Responda 'si' o 'no' ) " );
            BufferedReader reader = new BufferedReader( new InputStreamReader( System.in ) );
            String input = reader.readLine( ).toLowerCase( );
            boolean respuesta = false;
            if( input.equals( "si" ) || input.equals( "sí" ) || input.equals( "s" ) )
                respuesta = true;

            return respuesta;
        }
        catch( IOException e )
        {
            System.out.println( "Error leyendo de la consola" );
        }
        return false;
    }

    protected int natural(String mensaje) {
        int res = -1;
        while (res < 0) {
            try {
                System.out.print(mensaje + ": ");
                BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
                String input = reader.readLine();
                res = Integer.parseInt(input);

                if (res <= 0) {
                    System.out.println("El número debe ser natural (mayor a 0).");
                    res = -1;
                }
            } catch (NumberFormatException k) {
                System.out.println("El valor digitado no es un número natural.");
            } catch (IOException z) {
                System.out.println("Hubo un error al leer la consola.");
            }
        }
        return res;
    }


    protected double real(String mensaje)
    {
        double res = Integer.MIN_VALUE;
        while (res == Integer.MIN_VALUE)
        {
            try
            {
                System.out.print( mensaje + ": " );
                BufferedReader reader = new BufferedReader( new InputStreamReader( System.in ) );
                String input = reader.readLine();
                double num = Double.parseDouble(input);
                res = num;
            }
            catch(NumberFormatException k)
            {
                System.out.println("Lo digitado no es un número real.");
            }
            catch(IOException z)
            {
                System.out.println("Hubo un error al leer la consola.");
            }
        }
        return res;
    }
    
    public List<String> lista(String mensaje) {
        List<String> lista = new ArrayList<>();
        String respuesta = "s";

        while (respuesta.equalsIgnoreCase("s")) {
            String input = cadena(mensaje);
            lista.add(input);
            respuesta = cadena("¿Desea agregar otro elemento? (s/n)");
        }
        return lista;
    }
    
    public String revisarSetString(Set<String> conjuntoValido, String mensaje) {
    	String input = cadena(mensaje);
    	if (conjuntoValido.contains(input.toUpperCase())) {
    		return input.toUpperCase();
    	}
    	System.out.println("La opción ingresada no es válida.");
    	return revisarSetString(conjuntoValido, mensaje);
    }


}
