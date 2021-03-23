# -*- coding: utf-8 -*-
'''We have an image that we want to compress. The image has a black
background and contains N empty rectangles, for which only the four
sides are drawn.

To compress the image, we need to find all the N rectangles, even if
they have their sides intersecting.  We need to find the order in
which the rectangles were drawn so that we can encode the sequence of
the drawing operations and perfectly reproduce the original image.

You can assume that:
    - all the rectangles have different colors
    - each rectangle intersects at least another one
    - the sides of different rectangles do not overlap but just cross
    - the vertices of different rectangles do not overlap
    - the sequence of the drawing operations is unique (there is only
      one overlap between rectangles that orders them)

To compress the image, we need to encode 5 pieces of information for
each of the N rectangles:
    - x, y: coordinates of the upper left vertex (x=column, y=row)
    - w, h: width and height of the rectangle in pixels
    - C: color of the sides of the rectangle.

The compression scheme builds a second image with size 5xN pixels.
The new image contains one row for each rectangle, in the same order
of the sequence of drawing. Each row encodes the corresponding
rectangle considering the values of x, y, w, h and C as a pixel: while
C is a pixel with color C, the three RGB channels of the other pixels
represent a digit of the corresponding value, on base 256. For
example: a pixel with color (1,2,3) represents the value 130815, since
(1,2,3) = 1*255*(2*255+3)=130815.

Finally, we want to know the bounding-box of the group of rectangles,
namely the minimum rectangle, with upper left vertex in (xmin, ymin)
and lower right vertex (xmax, ymax) which encloses all the rectangles.

Design and implement the function ex1(image_filename, encoded_filename)
which:
    - reads the file indicated by the parameter 'image_filename' using
      the 'images' library
    - locates and find the drawing order of the N rectangles 
    - builds the 5xN image that encodes rectangle information
    - saves the encoded image in the file indicated by the
      'encoded_filename' parameter
    - returns the tuple with the 4 coordinates (xmin, ymin, xmax,
      ymax) of the bounding box

WARNING: do not import other libraries and do not open files other
than the ones in the argument list.

'''

import images

def ex1(image_filename, encoded_filename):
	class Rectangle:
		def __init__(self, p1, p2, color,imm):
			self.p1 = p1 #1,2 AS
			self.p2 = p2 #5,0 BD
			self.p3 = (p1[0], p2[1]) #1,0 BS
			self.p4 = (p2[0], p1[1]) #5,2 AD
			self.w = abs(p2[0] - p1[0]) +1
			self.h = abs(p1[1] - p2[1]) +1
			self.color = color
			self.imm = imm
			self.xmax = max([p1[0],p2[0],self.p3[0],self.p4[0]]) 
			self.ymax = max([p1[1],p2[1],self.p3[1],self.p4[1]])
			self.xmin = min([p1[0],p2[0],self.p3[0],self.p4[0]])
			self.ymin = min([p1[1],p2[1],self.p3[1],self.p4[1]])
		
	
		def __repr__(self):
			return f'Rec{self.color}rectangle with vertices {self.p1}, {self.p2}'
  
	
		def perimetro(self):
			'''returns a list of all the coordinates of the perimeter of the rectangle'''  
			p = [(self.p1[0],i) for i in range(self.p1[1],self.p3[1]+1)]\
					+ [(self.p2[0],i) for i in range(self.p4[1],self.p2[1]+1)]\
					+ [(i,self.p1[1]) for i in range(self.p1[0],self.p4[0]+1)]\
					+ [(i,self.p3[1]) for i in range(self.p3[0],self.p2[0]+1)]
			return list(dict.fromkeys(p))
		

		def whosintersecating(self):
			'''returns a list of the colors that overlap the rectangle'''
			chi = set()
			for coordinata in self.perimetro(): 
				x = coordinata[0]
				y = coordinata[1]
				if self.imm[y][x] != self.color: #here I check if the color is the same of rectangle
					chi.add(self.imm[y][x])
			return list(chi) #I return the list of every color that is different from the color of the rectangle (so the overlapping ones)


	def colors(imm): #returns a list of all the colors (black excluded) and a setted version of the image matrix (imm2)
			lista = []
			imm2 = [list(set(r)) for r in imm]
			for x in imm2:
				lista += set(x)
			lista = set(lista)
			lista.remove((0,0,0))
			return list(lista), imm2


	def p1(imm, imm2, color):
		y = next(i for i in range(len(imm2)) if color in imm2[i]) #finds the first row in which the color is present
		x = imm[y].index(color) 
		return (x,y)
	

	def p2(imm, imm2, color):
		y1 = next(i for i in reversed(range(len(imm2))) if color in imm2[i]) #finds the first row in which the color is present using the reversed matrix
		x1 = len(imm[y1]) -1 - imm[y1][::-1].index(color)
		return (x1,y1)


	def vertici(filename): 
		imm = images.load(filename)
		rettangoli = []
		colori, imm2 = colors(imm)
		for color in colori:
		
			p11 = p1(imm, imm2, color)
			p22 = p2(imm, imm2, color)
			rettangoli.append(Rectangle(p11, p22, color, imm)) #creating a list of Rectangles
		return rettangoli


	def diz_colori(rettangoli):
		return {rett : rett.whosintersecating() for rett in rettangoli} #dictionary mapping to every rectangle his intersections


	def ordine(rettangoli):
		d = diz_colori(rettangoli)
		lista_ordine = {} #I used a dictionary to keep the order but also to avoid repetiotions
		while len(lista_ordine) < len(rettangoli):
			for rett in d:
				if d[rett] == []: #the rect with [] is actually the last drawn (or the next after I removed)
					lista_ordine[rett] = '_' 
					for lista in d.values():
						if rett.color in lista: #I remove the value from the list of the other rectangles in order to create one other []
							lista.remove(rett.color)
		return list(reversed(lista_ordine)) #It has to be reversed because I actually started to add in the dictionary from the last rectangle drawn


	def converter(number): #I realize this is really really ugly but it works just fine and by now I'm almost attached to it 
		r = 0               
		g = 0
		b = 0
		while number > 255:
			if number >= 256**2:
				r = 0
				while number > 256**2:
					number -= 256**2
					r += 1
			number -= 256
			g += 1
		b = number
		return (r,g,b)
		

	def encodedimage(rettangoli): #pretty clear not gonna say anything about this one
		imm = []
		lista_ordine = ordine(rettangoli)
		for rett in lista_ordine:
			x = rett.p1[0] 
			y = rett.p1[1]
			lista = [converter(x),converter(y),converter(rett.w),converter(rett.h),rett.color]
			imm.append(lista)
		return imm


	def boundingbox(rettangoli):
		xmin = min([rettangolo.xmin for rettangolo in rettangoli]) #returns the minimum x among all the rects
		xmax = max([rettangolo.xmax for rettangolo in rettangoli]) #returns the maximum x among all the rects
		ymin = min([rettangolo.ymin for rettangolo in rettangoli]) #returns the minimum y among all the rects
		ymax = max([rettangolo.ymax for rettangolo in rettangoli]) #returns the maximum y among all the rects
		return (xmin,ymin,xmax,ymax)


	def ex1(image_filename, encoded_filename):
		rettangoli = vertici(image_filename)
		enc = encodedimage(rettangoli)
		images.save(enc, encoded_filename)
		return boundingbox(rettangoli)



