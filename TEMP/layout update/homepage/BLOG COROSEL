// src/components/Homepage/BlogCarousel.tsx
'use client';

import { useState, useRef } from 'react';
import Image from 'next/image';
import Link from 'next/link';
import { BlogMetadata } from '@/types/blog';

interface BlogCarouselProps {
  posts: BlogMetadata[];
}

export default function BlogCarousel({ posts }: BlogCarouselProps) {
  const [currentPage, setCurrentPage] = useState(0);
  const touchStartX = useRef(0);
  const touchEndX = useRef(0);
  const containerRef = useRef<HTMLDivElement>(null);
  
  const featuredPosts = posts.slice(0, 12);
  
  if (!featuredPosts || featuredPosts.length === 0) {
    return null;
  }

  // Desktop: 3 cards per page
  const cardsPerPageDesktop = 3;
  const totalPagesDesktop = Math.ceil(featuredPosts.length / cardsPerPageDesktop);
  
  // Mobile: 1 card per page
  const cardsPerPageMobile = 1;
  const totalPagesMobile = featuredPosts.length;

  const handleNext = () => {
    setCurrentPage(prev => {
      const totalPages = window.innerWidth >= 768 ? totalPagesDesktop : totalPagesMobile;
      return prev < totalPages - 1 ? prev + 1 : prev;
    });
  };
  
  const handlePrev = () => {
    setCurrentPage(prev => prev > 0 ? prev - 1 : prev);
  };

  const handleTouchStart = (e: React.TouchEvent) => {
    touchStartX.current = e.touches[0].clientX;
  };

  const handleTouchMove = (e: React.TouchEvent) => {
    touchEndX.current = e.touches[0].clientX;
  };

  const handleTouchEnd = () => {
    const diff = touchStartX.current - touchEndX.current;
    if (Math.abs(diff) > 75) {
      if (diff > 0) {
        handleNext();
      } else {
        handlePrev();
      }
    }
  };

  const handleMouseDown = (e: React.MouseEvent) => {
    e.preventDefault();
    const startX = e.clientX;
    let hasMoved = false;
    
    const handleMouseMove = (moveE: MouseEvent) => {
      const diff = startX - moveE.clientX;
      if (Math.abs(diff) > 75) {
        hasMoved = true;
        if (diff > 0) {
          handleNext();
        } else {
          handlePrev();
        }
        document.removeEventListener('mousemove', handleMouseMove);
      }
    };
    
    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', () => {
      document.removeEventListener('mousemove', handleMouseMove);
    }, { once: true });
  };

  // Calculate transform for desktop (3 cards + peek)
  const getDesktopTransform = () => {
    return `translateX(-${currentPage * 100}%)`;
  };

  // Calculate transform for mobile (1 card + peek)
  const getMobileTransform = () => {
    return `translateX(-${currentPage * 90}%)`;
  };

  return (
    <section className="bg-background py-12 md:py-16">
      {/* Section Title with Full-Width Lines */}
      <div className="px-6 md:px-8 lg:px-16 mb-8">
        <div className="w-full h-[1px] bg-border-color mb-4" />
        <h2 className="font-product text-xl md:text-2xl text-foreground text-center tracking-wider">
          BLOG SECTION
        </h2>
        <div className="w-full h-[1px] bg-border-color mt-4" />
      </div>
      
      {/* Desktop Pagination with Arrows */}
      <div className="hidden md:flex justify-end items-center gap-4 px-6 md:px-8 lg:px-16 mb-6">
        <button 
          onClick={handlePrev}
          disabled={currentPage === 0}
          className="text-foreground disabled:opacity-30 hover:opacity-70 transition-opacity"
          aria-label="Previous"
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <polyline points="15 18 9 12 15 6" />
          </svg>
        </button>
        <span className="font-product text-base text-foreground tracking-wider">
          {currentPage + 1} / {totalPagesDesktop}
        </span>
        <button 
          onClick={handleNext}
          disabled={currentPage === totalPagesDesktop - 1}
          className="text-foreground disabled:opacity-30 hover:opacity-70 transition-opacity"
          aria-label="Next"
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <polyline points="9 18 15 12 9 6" />
          </svg>
        </button>
      </div>
      
      {/* Carousel Container */}
      <div className="relative px-6 md:px-8 lg:px-16">
        <div 
          ref={containerRef}
          className="overflow-hidden cursor-grab active:cursor-grabbing select-none"
          onMouseDown={handleMouseDown}
          onTouchStart={handleTouchStart}
          onTouchMove={handleTouchMove}
          onTouchEnd={handleTouchEnd}
        >
          {/* Desktop: 3 cards + 4th peeking */}
          <div 
            className="hidden md:flex transition-transform duration-500 ease-out"
            style={{ 
              transform: getDesktopTransform(),
            }}
          >
            {Array.from({ length: totalPagesDesktop }).map((_, pageIndex) => (
              <div 
                key={pageIndex}
                className="flex-shrink-0 w-full flex gap-4"
              >
                {featuredPosts.slice(pageIndex * cardsPerPageDesktop, (pageIndex + 1) * cardsPerPageDesktop).map((post) => (
                  <div 
                    key={post.slug}
                    className="flex-shrink-0 w-[calc(33.33%-0.67rem)]"
                  >
                    <Link href={`/blog/${post.slug}`} className="block group">
                      {/* Image - 4:3 Ratio */}
                      <div className="relative w-full aspect-[4/3] mb-4">
                        {post.image && (
                          <Image
                            src={post.image}
                            alt={post.imageAlt || post.title}
                            fill
                            className="object-cover"
                            sizes="33vw"
                          />
                        )}
                      </div>
                      
                      {/* Category */}
                      {post.category && (
                        <p className="font-product uppercase text-xs text-foreground/70 mb-2 tracking-wider">
                          {post.category}
                        </p>
                      )}
                      
                      {/* Title */}
                      <h3 className="font-heading text-lg text-foreground mb-2 group-hover:opacity-70 transition-opacity line-clamp-2">
                        {post.title}
                      </h3>
                      
                      {/* Author */}
                      {post.author && (
                        <p className="font-product text-xs text-foreground/70 uppercase tracking-wider">
                          BY {post.author.toUpperCase()}
                        </p>
                      )}
                    </Link>
                  </div>
                ))}
              </div>
            ))}
          </div>

          {/* Mobile: 1 card + 2nd peeking */}
          <div 
            className="md:hidden flex transition-transform duration-500 ease-out"
            style={{ 
              transform: getMobileTransform(),
            }}
          >
            {featuredPosts.map((post) => (
              <div 
                key={post.slug}
                className="flex-shrink-0 w-[90%] pr-4"
              >
                <Link href={`/blog/${post.slug}`} className="block group">
                  {/* Image - 4:3 Ratio */}
                  <div className="relative w-full aspect-[4/3] mb-4">
                    {post.image && (
                      <Image
                        src={post.image}
                        alt={post.imageAlt || post.title}
                        fill
                        className="object-cover"
                        sizes="90vw"
                      />
                    )}
                  </div>
                  
                  {/* Category */}
                  {post.category && (
                    <p className="font-product uppercase text-xs text-foreground/70 mb-2 tracking-wider">
                      {post.category}
                    </p>
                  )}
                  
                  {/* Title */}
                  <h3 className="font-heading text-base text-foreground mb-2 group-hover:opacity-70 transition-opacity line-clamp-2">
                    {post.title}
                  </h3>
                  
                  {/* Author */}
                  {post.author && (
                    <p className="font-product text-xs text-foreground/70 uppercase tracking-wider">
                      BY {post.author.toUpperCase()}
                    </p>
                  )}
                </Link>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Mobile Pagination - Dots below carousel */}
      <div className="md:hidden flex justify-center gap-2 mt-6">
        {featuredPosts.map((_, index) => (
          <button
            key={index}
            onClick={() => setCurrentPage(index)}
            className={`w-2 h-2 rounded-full transition-colors ${
              index === currentPage ? 'bg-foreground' : 'bg-foreground/30'
            }`}
            aria-label={`Go to slide ${index + 1}`}
          />
        ))}
      </div>
    </section>
  );
}
