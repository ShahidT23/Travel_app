      ///////////////////////////////////////////////////////////////////////////////////////////////////////////

    // Searching From-To

    function swapValues() {
        var fromInput = document.getElementById('from');
        var toInput = document.getElementById('to');
        var tempValue = fromInput.value;
        fromInput.value = toInput.value;
        toInput.value = tempValue;
      }
      