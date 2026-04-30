// src/components/Inspo/FeaturedCarousel.tsx
'use client';

import { useState, useRef } from 'react';
import Link from 'next/link';
import type { DesignData } from '@/types/inspo';

interface FeaturedCarouselProps {
  designs: DesignData[];
}

export default function FeaturedCarousel({ designs }: FeaturedCarouselProps) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const scrollContainerRef = useRef<HTMLDivElement>(null);

  const scrollTo = (direction: 'left' | 'right') => {
    if (scrollContainerRef.current) {
      const cardWidth = scrollContainerRef.current.children[0]?.clientWidth || 0;
      const gap = 32;
      const scrollAmount = cardWidth + gap;
      
      if (direction === 'left') {
        scrollContainerRef.current.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        setCurrentIndex(Math.max(0, currentIndex - 1));
      } else {
        scrollContainerRef.current.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        setCurrentIndex(Math.min(designs.length - 1, currentIndex + 1));
      }
    }
  };

  return (
    <section className="py-16 md:py-20 bg-[#f9fafb]">
      <div className="max-w-7xl mx-auto px-6 md:px-12">
        <div className="flex items-center justify-between mb-12">
          <h2 
            className="text-[#252220]"
            style={{
              fontFamily: 'Larken, serif',
              fontSize: '32px',
              fontWeight: 400,
            }}
          >
            This Week's Styles
          </h2>
          
          <div className="hidden md:flex items-center gap-4">
            <button
              onClick={() => scrollTo('left')}
              disabled={currentIndex === 0}
              className="w-10 h-10 flex items-center justify-center border border-[#252220] hover:bg-[#252220] hover:text-[#f9fafb] transition-all disabled:opacity-30 disabled:cursor-not-allowed"
              aria-label="Previous"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
            </button>
            
            <span 
              className="text-[#252220]"
              style={{
                fontFamily: 'General Sans, sans-serif',
                fontSize: '14px',
              }}
            >
              {currentIndex + 1} / {designs.length}
            </span>
            
            <button
              onClick={() => scrollTo('right')}
              disabled={currentIndex === designs.length - 1}
              className="w-10 h-10 flex items-center justify-center border border-[#252220] hover:bg-[#252220] hover:text-[#f9fafb] transition-all disabled:opacity-30 disabled:cursor-not-allowed"
              aria-label="Next"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </button>
          </div>
        </div>

        <div
          ref={scrollContainerRef}
          className="flex gap-8 overflow-x-auto scrollbar-hide scroll-smooth snap-x snap-mandatory pb-4"
          style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
        >
          {designs.map((design) => (
            <Link
              key={design.slug}
              href={`/inspo/${design.slug}`}
              className="flex-shrink-0 w-[85%] md:w-[45%] lg:w-[30%] snap-start group"
            >
              <div className="relative overflow-hidden bg-[#f9fafb]">
                <div className="relative h-[400px] overflow-hidden">
                  <img
                    src={design.heroImage}
                    alt={design.displayName}
                    className="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700"
                  />
                </div>

                <div className="pt-4">
                  <p 
                    className="text-[#252220] mb-2"
                    style={{
                      fontFamily: 'General Sans, sans-serif',
                      fontSize: '12px',
                      textTransform: 'uppercase',
                      letterSpacing: '0.05em',
                    }}
                  >
                    {design.category}
                  </p>
                  <h3 
                    className="text-[#252220] group-hover:opacity-70 transition-opacity"
                    style={{
                      fontFamily: 'Larken, serif',
                      fontSize: '24px',
                      fontWeight: 400,
                    }}
                  >
                    {design.displayName}
                  </h3>
                </div>
              </div>
            </Link>
          ))}
        </div>

        <div className="flex md:hidden justify-center gap-2 mt-6">
          {designs.map((_, index) => (
            <button
              key={index}
              onClick={() => {
                setCurrentIndex(index);
                if (scrollContainerRef.current) {
                  const cardWidth = scrollContainerRef.current.children[0]?.clientWidth || 0;
                  const gap = 32;
                  scrollContainerRef.current.scrollTo({
                    left: (cardWidth + gap) * index,
                    behavior: 'smooth',
                  });
                }
              }}
              className={`h-1 rounded-full transition-all ${
                index === currentIndex ? 'w-8 bg-[#252220]' : 'w-1 bg-[#252220]/30'
              }`}
              aria-label={`Go to slide ${index + 1}`}
            />
          ))}
        </div>
      </div>
    </section>
  );
}
