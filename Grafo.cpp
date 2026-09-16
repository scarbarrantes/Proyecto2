#include "Grafo.h"
#include <iostream>

using namespace std;

Grafo::Grafo()
{
    // El grafo comienza vacío.
}

int Grafo::buscarServidor(const string& nombre)
{
    for (int i = 0; i < servidores.size(); i++)
    {
        if (servidores[i].nombre == nombre)
        {
            return i;
        }
    }

    return -1;
}

void Grafo::agregarServidor(const string& nombre)
{
    if (buscarServidor(nombre) != -1)
    {
        cout << "[INFO] El servidor " << nombre
             << " ya existe." << endl;

        return;
    }

    Servidor nuevoServidor;

    nuevoServidor.nombre = nombre;

    servidores.push_back(nuevoServidor);

    cout << "[OK] Servidor " << nombre
         << " agregado." << endl;
}

void Grafo::agregarConexion(const string& origen,
                            const string& destino,
                            int latencia)
{
    int posicionOrigen = buscarServidor(origen);
    int posicionDestino = buscarServidor(destino);

    if (posicionOrigen == -1 || posicionDestino == -1)
    {
        cout << "[ERROR] Uno o ambos servidores no existen."
             << endl;

        return;
    }

    Conexion nuevaConexion;

    nuevaConexion.destino = posicionDestino;
    nuevaConexion.latencia = latencia;

    servidores[posicionOrigen].conexiones.push_back(nuevaConexion);

    cout << "[OK] Conexion agregada: "
         << origen << " -> "
         << destino << " ("
         << latencia << " ms)" << endl;
}

void Grafo::mostrarGrafo()
{
    cout << endl;
    cout << "========== GRAFO DE RED ==========" << endl;

    if (servidores.empty())
    {
        cout << "El grafo esta vacio." << endl;
        return;
    }

    for (int i = 0; i < servidores.size(); i++)
    {
        cout << servidores[i].nombre << " -> ";

        if (servidores[i].conexiones.empty())
        {
            cout << "Sin conexiones";
        }
        else
        {
            for (int j = 0;
                 j < servidores[i].conexiones.size();
                 j++)
            {
                int destino =
                    servidores[i].conexiones[j].destino;

                int latencia =
                    servidores[i].conexiones[j].latencia;

                cout << servidores[destino].nombre
                     << " (" << latencia << " ms)";

                if (j + 1 <
                    servidores[i].conexiones.size())
                {
                    cout << ", ";
                }
            }
        }

        cout << endl;
    }

    cout << "==================================" << endl;
}
