/* Copyright (C) 2014 Embecosm Limited and University of Bristol

   Contributor James Pallister <james.pallister@bristol.ac.uk>

   This file is part of the Bristol/Embecosm Embedded Benchmark Suite.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program. If not, see <http://www.gnu.org/licenses/>. */

#include <support.h>

unsigned long cycles1;

void initialise_board()
{
}

void start_trigger()
{
    asm volatile ("rdcycle %0" : "=r" (cycles1));

}

void stop_trigger()
{
  unsigned long cycles2;
  asm volatile ("rdcycle %0" : "=r" (cycles2));
  printf("Runtime: %lu cycles\r\n", cycles2-cycles1);
}
