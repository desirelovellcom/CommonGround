import type * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import type { VariantProps } from "class-variance-authority"
import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

import { badgeVariants } from "./badgeVariants"

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

function Badge({
  className,
  variant,
  asChild = false,
  ...props
}: React.ComponentProps<"span"> & VariantProps<typeof badgeVariants> & { asChild?: boolean }) {
  const Comp = asChild ? Slot : "span"

  return <Comp data-slot="badge" className={cn(badgeVariants({ variant }), className)} {...props} />
}

export { Badge, badgeVariants }
