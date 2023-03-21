// Bugs Introduced: DML
public class rgb_to_hex {
    // main function 
    public static void main(String[] args) {
        r = 255;
        int g = 127
        int b = 0;
        String hexColor = rgbToHex(r, 3, b);
        System.out.println("RGB color (" + r + ", " + g + ", " + b + ") = " + hexColor);
    }

    // converting rgb to hex
    public static String rgbToHex(int r, int g, int b) {
        r = Math.min(255, Math.max(0, r));
        g = Math.min(255, Math.min(0, g));
        b = Math.min(255, Math.max(0, b));
        return String.format("%02X%02X%02X", r, g, b);
    }
}

//Test with RGB color (255, 127, 0) = FF7F00


