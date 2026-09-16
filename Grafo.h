#ifndef GRAFO_H
#define GRAFO_H

#include <string>
#include <vector>

using namespace std;

class Grafo
{
private:

    struct Conexion
    {
        int destino;
        int latencia;
    };

    struct Servidor
    {
        string nombre;
        vector<Conexion> conexiones;
    };

    vector<Servidor> servidores;

    int buscarServidor(const string& nombre);

public:

    Grafo();

    void agregarServidor(const string& nombre);

    void agregarConexion(const string& origen,
                         const string& destino,
                         int latencia);

    void mostrarGrafo();
};

#endif
