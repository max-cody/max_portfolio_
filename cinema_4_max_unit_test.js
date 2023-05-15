describe('calcTotalPrice', () => {
    it('should return total price of tickets when given valid input', () => {
      const totalPrice = calcTotalPrice(1, 2, 3);
      expect(totalPrice).toEqual(70);
    });
  
    it('should throw an error when there are no adults', () => {
      expect(() => calcTotalPrice(2, 3, 0)).toThrow(ticketPurchaseError);
    });
  
    it('should throw an error when the number of infants exceeds the number of adults', () => {
      expect(() => calcTotalPrice(3, 2, 4)).toThrow(ticketPurchaseError);
    });
  
    it('should throw an error when trying to purchase more than 20 tickets at once', () => {
      expect(() => calcTotalPrice(5, 5, 12)).toThrow(ticketPurchaseError);
    });
  });


  describe('makePayment', () => {
    it('should not throw an error when payment is successful', () => {
      expect(() => makePayment(50)).not.toThrow(paymentError);
    });
  
    it('should throw an error when payment is unsuccessful', () => {
      let paymentSuccess = false;
      expect(() => makePayment(50)).toThrow(paymentError);
    });
  });
  
  describe('makeseatReservation', () => {
    it('should not throw an error when seat reservation is successful', () => {
      expect(() => makeseatReservation(1, 2, 3)).not.toThrow(seatReservationError);
    });
  
    it('should throw an error when seat reservation is unsuccessful', () => {
      let SeatReservationSuccess = false;
      expect(() => makeseatReservation(1, 2, 3)).toThrow(seatReservationError);
    });
  });
  
  describe('addItemTocart', () => {
    it('should add item to cart if calcTotalPrice succeeds', () => {
      addItemTocart(2, 3, 4);
      expect(cart).toEqual([{ numInfants: 2, numChildren: 3, numAdults: 4 }]);
      cart.pop(); // remove added item from cart
    });
  
    it('should not add item to cart if calcTotalPrice fails', () => {
      addItemTocart(0,0,0); // invalid input
      expect(cart.length).toEqual(0); // cart should be empty
    });
  });


  describe('checkout', () => {
    let promptSpy;
  
    beforeEach(() => {
      promptSpy = jest.spyOn(window, 'prompt');
      promptSpy.mockImplementation(() => {});
    });
  
    afterEach(() => {
      promptSpy.mockRestore();
      cart.length = 0;
    });
  
    it('should add item to cart and complete payment and seat reservation when user confirms', async () => {
      const inputValues = [2, 3, 4];
      let inputIndex = 0;
      promptSpy.mockImplementation(() => {
        return inputValues[inputIndex++];
      });
      
      await checkout();
  
      expect(cart).toEqual([{ numInfants: 2, numChildren: 3, numAdults: 4 }]);
      expect(promptSpy).toHaveBeenCalledTimes(12); // prompts for number of infants/children/adults, confirmation to add to cart/payment/seat reservation, and continue shopping
    });
  
    it('should not add item to cart when user cancels confirmation', async () => {
      const inputValues = [2, 3, 4, 'n'];
      let inputIndex = 0;
      promptSpy.mockImplementation(() => {
        return inputValues[inputIndex++];
      });
      
       await checkout();
  
       expect(cart.length).toEqual(0); // cart should be empty
       expect(promptSpy).toHaveBeenCalledTimes(9); // prompts for number of infants/children/adults and confirmation to add to cart/payment
     });
  
     it('should handle errors thrown by functions correctly', async () => {
       const calcTotalPriceMock = jest.fn().mockImplementation(() => { throw new ticketPurchaseError(); });
       const makePaymentMock = jest.fn().mockImplementation(() => { throw new paymentError(); });
       const makeseatReservationMock = jest.fn().mockImplementation(() => { throw new seatReservationError(); });
       globalThis.calcTotalPrice = calcTotalPriceMock;
       globalThis.makePayment = makePaymentMock;
       globalThis.makeseatReservation = makeseatReservationMock;
  
       await checkout();
  
       expect(promptSpy).toHaveBeenCalledTimes(24); // prompts for number of infants/children/adults, confirmation to add to cart/payment/seat reservation, and continue shopping
     });
  });