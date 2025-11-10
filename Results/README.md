Após a análise dos três modelos treinados, conclui-se que o modelo com 100 épocas e batch size 32 atingiu a melhor performance global, com um mAP50 de 94.4% e mAP50-95 de 58.5%. Este modelo também apresenta as menores perdas de validação (box_loss: 1.229, cls_loss: 0.540), indicando uma boa generalização e menor overfitting.

A evolução do treino demonstrou que:

    ✅ Aumento de 50 para 100 épocas trouxe melhorias consistentes (+1.6% mAP50)

    ✅ Batch size 32 vs 16 proporcionou ganhos adicionais em estabilidade e métricas finais

    ✅ Não foram observados sinais claros de overfitting - as curvas de validação acompanharam consistentemente o treino

Limitações identificadas:

    ⚠️ Sensibilidade a condições de iluminação extremas (luz forte/contraste elevado)

    ⚠️ Falsos positivos em animais e estruturas com silhuetas humanoides


Conclusão: O modelo atual representa uma base sólida para desenvolvimento futuro, mas requer fine-tuning adicional (ajuste de learning rate, expansão do dataset com cenários desafiantes) antes de implementação em cenários reais de emergência
