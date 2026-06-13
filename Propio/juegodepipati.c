//Juego en C del ppt acerca de C
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int jugador, computadora, rondas = 0, victoriasJugador = 0, victoriasPC = 0;
    char opciones[3][20] = {"🪨 PIEDRA", "📄 PAPEL", "✂️  TIJERA"};
    
    srand(time(NULL));
    
    printf("⚔️=== PIEDRA, PAPEL O TIJERA ===⚔️\n");
    printf("1 = 🪨 PIEDRA | 2 = 📄 PAPEL | 3 = ✂️ TIJERA\n\n");
    
    while(victoriasJugador < 3 && victoriasPC < 3) {
        rondas++;
        
        printf("🔥 RONDA %d 🔥\n", rondas);
        printf("Tu elección (1-3): ");
        scanf("%d", &jugador);
        
        computadora = rand() % 3 + 1;
        
        printf("Tú: %s | PC: %s\n", opciones[jugador-1], opciones[computadora-1]);
        
        // Lógica del juego
        if(jugador == computadora) {
            printf("🤝 ¡EMPATE!\n\n");
        }
        else if(
            (jugador == 1 && computadora == 3) || // Piedra gana Tijera
            (jugador == 2 && computadora == 1) || // Papel gana Piedra
            (jugador == 3 && computadora == 2)    // Tijera gana Papel
        ) {
            printf("🎉 ¡TÚ GANAS esta ronda! 🎉\n");
            victoriasJugador++;
            printf("Tus victorias: %d | PC: %d\n\n", victoriasJugador, victoriasPC);
        }
        else {
            printf("😈 ¡PC GANA esta ronda! 😈\n");
            victoriasPC++;
            printf("Tus victorias: %d | PC: %d\n\n", victoriasJugador, victoriasPC);
        }
    }
    
    if(victoriasJugador == 3) {
        printf("🏆 ¡ERES EL CAMPEÓN! 🏆\n");
    } else {
        printf("🤖 ¡LA MÁQUINA HA GANADO! 🤖\n");
    }
    
    printf("\n¡Gracias por jugar! 🎮\n");
    return 0;
}