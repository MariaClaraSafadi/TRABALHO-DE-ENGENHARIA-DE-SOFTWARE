function ehPrimo(numero) {
    if (numero <= 1) return false;
    if (numero === 2) return true;
    for (let i = 2; i <= Math.sqrt(numero); i++) {
      if (numero % i === 0) return false;
    }
    return true;
  }
  
  const numero = 17;
  console.log(`O número ${numero} é primo?`, ehPrimo(numero));
  