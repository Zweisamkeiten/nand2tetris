// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.
  (START)
    @255
    D=A
    @maxrow
    M=D

    @state
    M=0 // state: if filled: state == 1; if cleared: state == 0;

    (LOOP)
      @KBD
      D=M
      @FILL
      D;JGT // if KBD > 0: goto fill the screen

      @KBD
      D=M
      @CLEAR
      D;JEQ // if KBD == 0: goto clear the screen

      (RETURN)
      @LOOP
      0;JMP




  (FILL)
    @state
    M=1

    @SCREEN
    D=A
    @address
    M=D

    @row
    M=0
    @column
    M=0

    (FILLLOOP)
      @row
      D=M
      @maxrow
      D=D-M
      @RETURN
      D;JEQ // if i == maxrow goto END

      @address
      A=M
      M=-1  // RAM[address] = -1 (16 pixels)
      @address
      M=M+1 // address++

      @column
      M=M+1 // column = column + 1
      D=M
      @32
      D=D-A
      @FILLRESETCOLUMNANDADDROW
      D;JEQ  // if column == 32: column = 0; row++;

      @FILLLOOP
      0;JMP

    (FILLRESETCOLUMNANDADDROW)
      @column
      M=0
      @row
      M=M+1
      @FILLLOOP
      0;JMP

  (CLEAR)
    @state
    M=0

    @SCREEN
    D=A
    @address
    M=D

    @row
    M=0
    @column
    M=0

    (CLEARLOOP)
      @row
      D=M
      @maxrow
      D=D-M
      @RETURN
      D;JEQ // if i == maxrow goto END

      @address
      A=M
      M=0  // RAM[address] = 0 (16 pixels)
      @address
      M=M+1 // address++

      @column
      M=M+1 // column = column + 1
      D=M
      @32
      D=D-A
      @CLEARRESETCOLUMNANDADDROW
      D;JEQ  // if column == 32: column = 0; row++;

      @CLEARLOOP
      0;JMP

    (CLEARRESETCOLUMNANDADDROW)
      @column
      M=0
      @row
      M=M+1
      @CLEARLOOP
      0;JMP
