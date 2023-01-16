armstrong = (()=>{
    const EXPOENTE = 3;
    const arrayOfArmstrongNumbers = [];
    for (centena=0; centena<=9; centena++){
      for (dezena=0; dezena<=9; dezena++){
        for (unidade=0; unidade<=9; unidade++){
          let numero = centena*100 + dezena*10 + unidade;
          let calculoArmstrong = Math.pow(centena, EXPOENTE) + Math.pow(dezena, EXPOENTE) + Math.pow(unidade, EXPOENTE);
          if (numero === calculoArmstrong){
              arrayOfArmstrongNumbers.push(numero);
              console.log(numero)
          }
        }
      }
    }
    return arrayOfArmstrongNumbers;
  })()