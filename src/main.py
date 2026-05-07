import argparse

from reconstructor import recreate_with_rectangles


def main():
    parser = argparse.ArgumentParser(description='Genera una recreación artística usando rectángulos.')
    parser.add_argument('--input', '-i', required=True, help='Ruta de la imagen de entrada')
    parser.add_argument('--output', '-o', required=True, help='Ruta del archivo de salida')
    parser.add_argument('--rects', '-r', type=int, default=25, help='Cantidad de rectángulos a usar (default: 25)')

    args = parser.parse_args()
    print(f'Imagen de entrada: {args.input}')
    print(f'Salida: {args.output}')
    print(f'Rectángulos: {args.rects}')

    recreate_with_rectangles(args.input, args.output, args.rects)

if __name__ == '__main__':
    main()