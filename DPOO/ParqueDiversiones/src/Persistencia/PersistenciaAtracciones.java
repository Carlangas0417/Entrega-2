package Persistencia;

import java.io.ObjectOutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;


import CatalogoAtracciones.Atraccion;

public class PersistenciaAtracciones implements Persistencia {
	
    public static void guardarAtraccion(Atraccion atraccion, String archivo) throws Exception {
        ObjectOutputStream output = new ObjectOutputStream(new FileOutputStream(new File(dirArchivo + archivo)));
        output.writeObject(atraccion);
        output.close();
    }

    public static Atraccion cargarAtraccion(String archivo) throws Exception {
        Atraccion atraccion = null;
        if (Files.exists(Paths.get(dirArchivo + archivo))) {
            ObjectInputStream input = new ObjectInputStream(
                    new FileInputStream(new File(dirArchivo + archivo)));
            atraccion = (Atraccion) input.readObject();
            input.close();
        } else {
        	System.out.println("El archivo no existe. No se cargó ninguna atracción.");
        }
        return atraccion;  
	}
}
