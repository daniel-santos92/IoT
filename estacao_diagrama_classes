# Diagrama de Classes

## Classes e Atributos

### Sensor
| Atributos             | Métodos                  |
|-----------------------|---------------------------|
| `id: String`          | `+ coletarDados(): void`  |
| `tipo: String`        | `+ enviarDados(): void`   |
| `valorAtual: Float`   |                           |

**Classe Base** para sensores específicos.

---

### TemperaturaSolo
| Atributos             | Métodos                  |
|-----------------------|---------------------------|
| `valor: Float`        | `+ coletarDados(): void`  |
|                       | `+ enviarDados(): void`   |

**Herda de:** `Sensor`

---

### UmidadeSolo
| Atributos             | Métodos                  |
|-----------------------|---------------------------|
| `valor: Float`        | `+ coletarDados(): void`  |
|                       | `+ enviarDados(): void`   |

**Herda de:** `Sensor`

---

### TemperaturaAr
| Atributos             | Métodos                  |
|-----------------------|---------------------------|
| `valor: Float`        | `+ coletarDados(): void`  |
|                       | `+ enviarDados(): void`   |

**Herda de:** `Sensor`

---

### UmidadeAr
| Atributos             | Métodos                  |
|-----------------------|---------------------------|
| `valor: Float`        | `+ coletarDados(): void`  |
|                       | `+ enviarDados(): void`   |

**Herda de:** `Sensor`

---

### PressaoAtmosferica
| Atributos             | Métodos                  |
|-----------------------|---------------------------|
| `valor: Float`        | `+ coletarDados(): void`  |
|                       | `+ enviarDados(): void`   |

**Herda de:** `Sensor`

---

### Luminosidade
| Atributos             | Métodos                  |
|-----------------------|---------------------------|
| `valor: Float`        | `+ coletarDados(): void`  |
|                       | `+ enviarDados(): void`   |

**Herda de:** `Sensor`

---

### VelocidadeVento
| Atributos             | Métodos                  |
|-----------------------|---------------------------|
| `valor: Float`        | `+ coletarDados(): void`  |
|                       | `+ enviarDados(): void`   |

**Herda de:** `Sensor`

---

### DirecaoVento
| Atributos             | Métodos                  |
|-----------------------|---------------------------|
| `valor: Float`        | `+ coletarDados(): void`  |
|                       | `+ enviarDados(): void`   |

**Herda de:** `Sensor`

---

### IndicadorChuva
| Atributos             | Métodos                  |
|-----------------------|---------------------------|
| `valor: Boolean`      | `+ coletarDados(): void`  |
|                       | `+ enviarDados(): void`   |

**Herda de:** `Sensor`

---

### Camera
| Atributos             | Métodos                    |
|-----------------------|----------------------------|
| `id: String`          | `+ capturarImagem(): Imagem` |
| `descricao: String`  | `+ enviarImagem(): void`    |

---

### Imagem
| Atributos             | Métodos                     |
|-----------------------|------------------------------|
| `id: String`          | `+ processarImagem(): void`  |
| `dataHora: Date`      |                              |
| `dadosImagem: BYTEA`  |                              |

---

### ServidorNuvem
| Atributos              | Métodos                                      |
|------------------------|----------------------------------------------|
| `dados: List<Dado>`    | `+ receberDados(dado: Dado): void`           |
| `imagens: List<Imagem>` | `+ receberImagem(imagem: Imagem): void`    |
|                        | `+ agruparDados(): void`                    |
|                        | `+ fornecerDadosParaAplicativo(): void`     |

---

### InterfaceWeb
| Atributos             | Métodos                                      |
|-----------------------|----------------------------------------------|
| `grafico: Grafico`    | `+ mostrarGrafico(dados: List<Dado>): void` |

---

### AplicativoSmartphone
| Atributos              | Métodos                                |
|------------------------|----------------------------------------|
| `dadosAgrupados: List<Dado>` | `+ exibirDados(dados: List<Dado>): void` |

---

### Dado
| Atributos             | Métodos                  |
|-----------------------|---------------------------|
| `id: String`          | `+ processarDado(): void` |
| `sensorId: String`    |                           |
| `dataHora: Date`      |                           |
| `valor: Float`        |                           |

---

## Relações Entre Classes

- **Sensor** é a classe base para todas as classes de sensores específicos (e.g., `TemperaturaSolo`, `UmidadeSolo`, etc.).
- **Camera** captura **Imagem** e envia para **ServidorNuvem**.
- **ServidorNuvem** armazena **Dado** e **Imagem** e fornece dados agrupados para **InterfaceWeb** e **AplicativoSmartphone**.
- **InterfaceWeb** mostra gráficos baseados em **Dado**.
- **AplicativoSmartphone** consome dados agrupados fornecidos por **ServidorNuvem**.
