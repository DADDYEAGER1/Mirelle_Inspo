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
  const [isDragging, setIsDragging] = useState(false);
  const dragStartX = useRef(0);
  const dragOffset = useRef(0);
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

  // Touch/Drag handlers for smooth swipe
  const handleDragStart = (clientX: number) => {
    setIsDragging(true);
    dragStartX.current = clientX;
    dragOffset.current = 0;
  };

  const handleDragMove = (clientX: number) => {
    if (!isDragging) return;
    dragOffset.current = clientX - dragStartX.current;
  };

  const handleDragEnd = () => {
    if (!isDragging) return;
    setIsDragging(false);
    
    const threshold = 75;
    if (Math.abs(dragOffset.current) > threshold) {
      if (dragOffset.current < 0) {
        handleNext();
      } else {
        handlePrev();
      }
    }
    dragOffset.current = 0;
  };

  // Mouse events
  const handleMouseDown = (e: React.MouseEvent) => {
    e.preventDefault();
    handleDragStart(e.clientX);
  };

  const handleMouseMove = (e: React.MouseEvent) => {
    handleDragMove(e.clientX);
  };

  const handleMouseUp = () => {
    handleDragEnd();
  };

  const handleMouseLeave = () => {
    if (isDragging) {
      handleDragEnd();
    }
  };

  // Touch events
  const handleTouchStart = (e: React.TouchEvent) => {
    handleDragStart(e.touches[0].clientX);
  };

  const handleTouchMove = (e: React.TouchEvent) => {
    handleDragMove(e.touches[0].clientX);
  };

  const handleTouchEnd = () => {
    handleDragEnd();
  };

  // Calculate transform for desktop (3 cards + peek)
  const getDesktopTransform = () => {
    const baseTransform = currentPage * 100;
    const dragPercent = isDragging ? (dragOffset.current / window.innerWidth) * 100 : 0;
    return `translateX(-${baseTransform - dragPercent}%)`;
  };

  // Calculate transform for mobile (1 card + peek)
  const getMobileTransform = () => {
    const baseTransform = currentPage * 90;
    const dragPercent = isDragging ? (dragOffset.current / window.innerWidth) * 90 : 0;
    return `translateX(-${baseTransform - dragPercent}%)`;
  };

  return (
    <section className="bg-background pt-16 md:pt-24 pb-8">
      {/* Section Title with Full-Width Lines */}
      <div className="mb-8 md:mb-12">
        <div className="w-full h-[1px] bg-foreground" />
        <div className="px-3 md:px-6 lg:px-12 py-6">
          <h2 className="font-ui text-base md:text-lg text-foreground text-center tracking-wider uppercase">
            BLOG SECTION
          </h2>
        </div>
        <div className="w-full h-[1px] bg-foreground" />
      </div>
      
      {/* Desktop Pagination with Arrows */}
      <div className="hidden md:flex justify-end items-center gap-4 px-3 md:px-6 lg:px-12 mb-6">
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
        <span className="font-ui text-sm text-foreground tracking-wider">
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
      <div className="relative px-3 md:px-6 lg:px-12">
        <div 
          ref={containerRef}
          className="overflow-visible cursor-grab active:cursor-grabbing select-none"
          onMouseDown={handleMouseDown}
          onMouseMove={handleMouseMove}
          onMouseUp={handleMouseUp}
          onMouseLeave={handleMouseLeave}
          onTouchStart={handleTouchStart}
          onTouchMove={handleTouchMove}
          onTouchEnd={handleTouchEnd}
        >
          {/* Desktop: 3 cards + 4th peeking */}
          <div className="hidden md:block overflow-hidden">
            <div 
              className="flex transition-transform ease-out"
              style={{ 
                transform: getDesktopTransform(),
                transitionDuration: isDragging ? '0ms' : '500ms',
              }}
            >
              {Array.from({ length: totalPagesDesktop }).map((_, pageIndex) => (
                <div 
                  key={pageIndex}
                  className="flex-shrink-0 w-full flex gap-6"
                >
                  {featuredPosts.slice(pageIndex * cardsPerPageDesktop, (pageIndex + 1) * cardsPerPageDesktop).map((post) => (
                    <div 
                      key={post.slug}
                      className="flex-shrink-0 w-[calc(33.33%-1rem)]"
                    >
                      <Link href={`/blog/${post.slug}`} className="block group">
                        {/* Image - 4:3 Ratio */}
                        <div className="relative w-full aspect-[4/3] mb-4 overflow-hidden">
                          {post.image && (
                            <Image
                              src={post.image}
                              alt={post.imageAlt || post.title}
                              fill
                              className="object-cover group-hover:scale-105 transition-transform duration-300"
                              sizes="33vw"
                              draggable={false}
                            />
                          )}
                        </div>
                        
                        {/* Category */}
                        {post.category && (
                          <p className="font-ui uppercase text-xs text-foreground/70 mb-2 tracking-wider">
                            {post.category}
                          </p>
                        )}
                        
                        {/* Title */}
                        <h3 className="font-heading text-xl text-foreground mb-2 group-hover:opacity-70 transition-opacity line-clamp-2">
                          {post.title}
                        </h3>
                        
                        {/* Author */}
                        {post.author && (
                          <p className="font-ui text-xs text-foreground/70 uppercase tracking-wider">
                            BY {post.author.toUpperCase()}
                          </p>
                        )}
                      </Link>
                    </div>
                  ))}
                </div>
              ))}
            </div>
          </div>

          {/* Mobile: 1 card + 2nd peeking */}
          <div 
            className="md:hidden flex transition-transform ease-out"
            style={{ 
              transform: getMobileTransform(),
              transitionDuration: isDragging ? '0ms' : '500ms',
            }}
          >
            {featuredPosts.map((post) => (
              <div 
                key={post.slug}
                className="flex-shrink-0 w-[90%] pr-4"
              >
                <Link href={`/blog/${post.slug}`} className="block group">
                  {/* Image - 4:3 Ratio */}
                  <div className="relative w-full aspect-[4/3] mb-4 overflow-hidden">
                    {post.image && (
                      <Image
                        src={post.image}
                        alt={post.imageAlt || post.title}
                        fill
                        className="object-cover group-hover:scale-105 transition-transform duration-300"
                        sizes="90vw"
                        draggable={false}
                      />
                    )}
                  </div>
                  
                  {/* Category */}
                  {post.category && (
                    <p className="font-ui uppercase text-xs text-foreground/70 mb-2 tracking-wider">
                      {post.category}
                    </p>
                  )}
                  
                  {/* Title */}
                  <h3 className="font-heading text-lg text-foreground mb-2 group-hover:opacity-70 transition-opacity line-clamp-2">
                    {post.title}
                  </h3>
                  
                  {/* Author */}
                  {post.author && (
                    <p className="font-ui text-xs text-foreground/70 uppercase tracking-wider">
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
      <div className="md:hidden flex justify-center gap-2 mt-6 px-3 md:px-6 lg:px-12">
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
